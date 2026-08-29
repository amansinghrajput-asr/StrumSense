# StrumSense — Step-by-Step Build Guide
### Build with भारत 2.0 — Hackathon Execution Plan

This is a practical, ordered guide to actually building the MVP described in the pitch deck and report. It assumes a typical 24–36 hour hackathon window and a team of 3–4 people who can split into an **Audio track**, a **Vision track**, and a **Frontend/Integration track**.

---

## 0. Before the Hackathon Starts (Prep Night)

- [ ] Install Python 3.10+ and Node (if using any JS tooling).
- [ ] Create the repo and a shared `requirements.txt` early so no one blocks on installs during the event.
- [ ] Pre-install the heavy libraries once, locally, and confirm they import cleanly:
  ```bash
  pip install streamlit opencv-python mediapipe librosa numpy soundfile streamlit-webrtc
  ```
- [ ] Agree on the **chord set for the demo** — keep it small. Recommended: `C, G, D, Em` (4 open chords, harmonically distinct, easy to strum cleanly).
- [ ] Assign roles: one person owns Audio, one owns Vision, one owns the Streamlit UI + fusion glue, one owns the Figma mockups + pitch deck.

---

## 1. Audio Engine — Chord Detection (4–6 hrs)

**Goal:** microphone input → chord name, using chroma matching (not raw FFT).

1. Capture short audio windows (e.g. 1–2 seconds) from the mic using `sounddevice` or Streamlit's audio input.
2. Compute a chroma feature per window:
   ```python
   import librosa
   chroma = librosa.feature.chroma_cqt(y=audio_window, sr=sample_rate)
   chroma_avg = chroma.mean(axis=1)  # 12-dim vector
   ```
3. Build **reference chroma templates** for your 4 chords by recording a clean strum of each and averaging its chroma vector. Store these as a small lookup table (a dict of chord name → 12-dim vector).
4. Classify each live window by **cosine similarity** to the templates; pick the closest match above a confidence threshold, otherwise output "no chord detected."
5. Smooth the output over 2–3 consecutive windows (majority vote) so it doesn't flicker between chords.

**Checkpoint:** you should be able to strum C, G, D, or Em and see the correct label printed in the terminal before moving to the UI.

---

## 2. Vision Engine — Strum Direction (4–6 hrs)

**Goal:** camera input → "UP" / "DOWN" for the strumming hand.

1. Open the webcam feed with OpenCV and pass frames to **MediaPipe Pose** (not full Hand landmarks — Pose is far more robust to the motion blur of fast strumming).
2. Track the **wrist landmark's Y-coordinate** frame to frame.
3. Compute the frame-to-frame Y-velocity. A negative velocity (Y decreasing, since image Y grows downward) beyond a small threshold = upstroke; positive = downstroke; near-zero = idle.
4. Debounce: only register a new strum direction after the velocity crosses zero and exceeds the threshold again, so a single stroke doesn't get counted twice.
5. Draw the tracked wrist point on the video feed so the live demo visually shows what's being tracked.

**Checkpoint:** wave your strumming hand up and down in front of the camera and confirm the terminal prints alternating UP/DOWN cleanly, without double-counting.

---

## 3. Fusion Layer — Keeping Audio and Vision in Sync (2–3 hrs)

This is the step most teams skip, and it's the one judges notice.

1. Timestamp every audio window and every vision frame as they're produced (`time.time()` or a shared clock).
2. On a fixed tick (e.g. every 100ms), take the **most recent chord label** and the **most recent strum direction** and combine them into one output: `"C Major – Downstroke"`.
3. If either stream hasn't updated in the last ~500ms, mark it stale rather than showing an outdated chord/direction as if it were live.

**Checkpoint:** strum a chord and confirm the combined label updates smoothly in near real time, without one stream lagging visibly behind the other.

---

## 4. Streamlit UI — Wiring It Together (3–4 hrs)

1. Use `streamlit-webrtc` (or a simple OpenCV `VideoCapture` loop with `st.image` in a `while` loop) to show the live camera feed.
2. Overlay the fused "Chord + Strum Direction" text on the video frame before displaying it.
3. Add a **Start/Stop Session** button. While a session is running, log every fused output with its timestamp to a list.
4. On Stop, render that log as a simple timeline table (`st.dataframe`) — this is your Session Recording feature, already demo-able live.

**Checkpoint:** click Start, strum a few chords, click Stop, and see a timeline table of what was played and when.

---

## 5. Newbie / Pro Mode — Figma Mockups (parallel track, 3–4 hrs)

These are **stretch features** — design them, don't try to fully implement them live:

- [ ] Newbie Mode screen: ghost-chord diagram overlay, metronome sync indicator, "Patience Mode" slow-down toggle.
- [ ] Pro Mode screen: auto-generated chord-sheet PDF preview, micro-timing graph (rushing vs. dragging vs. the beat).
- [ ] Progress Dashboard screen: a simple line chart mockup of accuracy/timing over multiple sessions.

Keep these visually consistent with the live app's color palette so the pitch feels like one coherent product, not two disconnected halves.

---

## 6. Demo Rehearsal & Backup Plan (1–2 hrs, do this — don't skip it)

- [ ] **Record a backup demo video** of the live app working end-to-end, well-lit, on the same hardware you'll present with. This is your insurance against mic/camera permission issues or bad hall lighting on stage.
- [ ] Rehearse the live demo at least twice, out loud, with the actual pitch narration.
- [ ] Prepare one sentence each for: the sync/fusion challenge, and why hybrid audio+vision beats audio-only competitors. Judges reward teams who can name their hardest technical problem clearly.

---

## 7. Final Packaging Checklist

- [ ] Clean chord set works reliably (C, G, D, Em minimum).
- [ ] Live demo boots in under 15 seconds.
- [ ] Backup demo video is ready and tested on the presentation laptop.
- [ ] GitHub repo is public (or accessible to judges) with a short README explaining setup.
- [ ] Pitch deck (`StrumSense_Build_with_Bharat_2.0.pptx`) has team name, members, and links filled in — remove any placeholder text.
- [ ] Project report (`StrumSense_Project_Report.docx`) links match the deck.
- [ ] Time-box a final 15-minute run-through of the whole pitch, start to finish, with a clock running.

---

## Suggested Time Allocation (24-hour window)

| Hours | Focus |
|---|---|
| 0–1 | Setup, repo, role split, chord set decision |
| 1–7 | Audio engine (parallel with Vision engine) |
| 1–7 | Vision engine (parallel with Audio engine) |
| 7–10 | Fusion layer + Streamlit UI wiring |
| 7–11 | Figma mockups for Newbie/Pro modes (parallel) |
| 11–14 | Integration testing, bug fixing |
| 14–16 | Session recording + timeline table |
| 16–18 | Record backup demo video |
| 18–20 | Pitch deck & report polish, fill in real team details |
| 20–22 | Rehearse pitch, fix anything broken |
| 22–24 | Buffer / sleep in shifts / final checklist |

Adjust freely — the order (Audio + Vision in parallel → Fusion → UI → Demo prep) matters more than the exact hour counts.
