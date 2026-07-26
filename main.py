import gifos

USERNAME = "jaweed3"

FONT = "JetBrainsMonoNerdFontMono-Regular.ttf"

t = gifos.Terminal(width=680, height=540, xpad=5, ypad=5, font_size=14)
t.set_font(FONT, 14)
t.set_fps(15)


def col(text, name):
    t.set_txt_color(name)
    t.gen_text(text, t.curr_row, contin=True)


def boot_line(text, color="white", delay=2, same=False):
    r = t.curr_row if same else t.curr_row + 1
    t.set_txt_color(color)
    t.gen_text(text, r)
    t.clone_frame(delay)
    t.set_txt_color("white")


def ok(text, delay=1):
    r = t.curr_row + 1
    t.set_txt_color("white")
    t.gen_text("  [", r)
    t.set_txt_color("green")
    t.gen_text("OK", r, contin=True)
    t.set_txt_color("white")
    t.gen_text("]", r, contin=True)
    t.set_txt_color("cyan")
    t.gen_text(text, r, contin=True)
    t.set_txt_color("white")
    t.clone_frame(delay)


def bar(pct, width=18):
    fill = int(pct / 100 * width)
    b = "\x1b[32m" + "\u2588" * fill + "\x1b[90m" + "\u2588" * (width - fill) + "\x1b[0m"
    return f"[{b}] {pct:3d}%"


def animate(text, row, step=4):
    for pct in range(0, 101, step):
        t.delete_row(row)
        t.gen_text(f"  {bar(pct)}  {text}", row)
        t.clone_frame(1)


def scroll(wait=10):
    t.clone_frame(wait)


# ====================================================================
# 1. ML Runtime Init
# ====================================================================
t.curr_row = 0
boot_line(f"{USERNAME} ML Runtime v0.4.2", delay=6)
ok(" ONNX Runtime 1.21.0")
ok(" CUDA 12.8 detected")
ok(" TensorRT 10.7")

r = t.curr_row + 1
t.set_txt_color("gray")
t.gen_text("  loading runtime kernels...", r)
for i in range(10, 101, 10):
    t.delete_row(r)
    t.gen_text(f"  loading runtime kernels... {i}%", r)
    t.clone_frame(1)
t.delete_row(r)
t.set_txt_color("green")
t.gen_text("  loading runtime kernels... done", r)
t.set_txt_color("white")
scroll(8)

animate("initializing compute graph", t.curr_row + 1)
scroll(8)

# ====================================================================
# 2. Model Load
# ====================================================================
boot_line("model ingest: rescuevision.onnx", delay=4)

r = t.curr_row + 1
t.set_txt_color("gray")
t.gen_text("  ├ architecture: YOLOv8n-seg", r)
r += 1
t.gen_text("  ├ input:  3x224x224  (RGB)", r)
r += 1
t.gen_text("  └ params: 3.27M", r)

r = t.curr_row + 1
summary = (
    "\x1b[90m      layer       out shape    params\x1b[0m\n"
    "\x1b[90m   \x1b[0m  conv1      64x112x112    1,856\n"
    "\x1b[90m   \x1b[0m  conv2     128x56x56     73,856\n"
    "\x1b[90m   \x1b[0m  c2f_1     128x56x56    197,632\n"
    "\x1b[90m   \x1b[0m  conv3     256x28x28    295,424\n"
    "\x1b[90m   \x1b[0m  c2f_2     256x28x28    591,872\n"
    "\x1b[90m   \x1b[0m  conv4     512x14x14    590,336\n"
    "\x1b[90m   \x1b[0m  c2f_3     512x14x14    591,872\n"
    "\x1b[90m   \x1b[0m  spp       512x14x14    262,400\n"
    "\x1b[90m   \x1b[0m  detekt    (84+32)x8400   55,296\n"
    "\x1b[90m   \x1b[0m  \x1b[33m--------------------------------\x1b[0m\n"
    "\x1b[90m   \x1b[0m  total                3,267,392"
)
t.gen_text(summary, r)
scroll(8)

animate("compiling graph", t.curr_row + 1)
scroll(5)

# ====================================================================
# 3. Quantization
# ====================================================================
boot_line("quantization: FP32 -> INT8", delay=3)
r = t.curr_row + 1
t.gen_text("  calibrating on 512 samples...", r)
scroll(4)

for pct in range(0, 101, 10):
    t.delete_row(t.curr_row)
    t.gen_text(f"  {bar(pct, 22)}  layer {pct//10 + 1}/10", t.curr_row)
    t.clone_frame(2)
scroll(5)

r = t.curr_row + 1
t.set_txt_color("gray")
t.gen_text("  model size:  12.47 MB  ->  3.12 MB", r)
r += 1
t.gen_text("  latency:     42.1 ms  ->  21.8 ms", r)
r += 1
t.gen_text("  accuracy:    0.893   ->  0.882", r)
r += 1
t.set_txt_color("green")
t.gen_text("  profile: edge_server_fast", r)
t.set_txt_color("white")
scroll(12)

# ====================================================================
# 4. Deploy to Edge  (clean frame)
# ====================================================================
t.clear_frame()
t.curr_row = 0

t.set_txt_color("cyan")
t.gen_text("              DEPLOY TARGET", 1)
t.set_txt_color("white")

box = (
    "\x1b[90m  \u250c──────────────────────────────────────────\u2510\x1b[0m\n"
    "\x1b[90m  \u2502\x1b[0m  device:   RescueVision v2 @ RPi 5      \x1b[90m\u2502\x1b[0m\n"
    "\x1b[90m  \u2502\x1b[0m  status:   \u001b[90mconnecting...\x1b[0m               \x1b[90m\u2502\x1b[0m\n"
    "\x1b[90m  \u2502\x1b[0m  protocol: USB-C / MIPI CSI             \x1b[90m\u2502\x1b[0m\n"
    "\x1b[90m  \u2502\x1b[0m  power:    5V 3A (15W)                   \x1b[90m\u2502\x1b[0m\n"
    "\x1b[90m  \u2514──────────────────────────────────────────\u2518\x1b[0m"
)
t.gen_text(box, 2)
scroll(8)

status_row = 4  # row within the box that has status
for pct in range(0, 101, 5):
    label = "connected" if pct >= 20 else "connecting..."
    c = "\x1b[32m" if pct >= 100 else "\x1b[93m" if pct >= 20 else "\x1b[90m"
    t.delete_row(status_row)
    t.gen_text(f"  \x1b[90m  \u2502\x1b[0m  status:   {c}{label}\x1b[0m{' ' * (20 - len(label))}\x1b[90m\u2502\x1b[0m", status_row)
    t.clone_frame(1)

t.delete_row(status_row)
t.gen_text(f"  \x1b[90m  \u2502\x1b[0m  status:   \x1b[32mconnected\x1b[0m                  \x1b[90m\u2502\x1b[0m", status_row)
scroll(5)

animate("deploying model to edge", t.curr_row + 1)
scroll(5)

t.set_txt_color("green")
t.gen_text("  inference pipeline ACTIVE  @  30 FPS", t.curr_row + 1)
t.set_txt_color("white")
scroll(15)

# ====================================================================
# 5. Login  (clean frame)
# ====================================================================
t.clear_frame()
t.curr_row = 0

t.set_txt_color("green")
t.gen_text("jaweed3", 1)
t.set_txt_color("white")
t.gen_text(" login: ", 1, contin=True)
t.gen_typing_text("jaweed3", 1, t.curr_col + 1, True, speed=0.1)
scroll(8)
t.set_txt_color("white")
t.gen_text("Password: ", 2)
t.gen_typing_text("********", 2, 11, True, speed=0.1)
scroll(12)

# ====================================================================
# 6. Welcome + showfetch
# ====================================================================
t.curr_row = 2
t.clone_frame(1)
t.delete_row(1)
t.delete_row(2)
t.gen_text("Welcome, Fatih!  Last login:  Sun Jul 26 00:00:01 WIB 2026", 1)

t.set_prompt(f"\x1b[35m{USERNAME}\x1b[39m@\x1b[32mgithub\x1b[39m:~$ ")
t.gen_prompt(2)
t.gen_typing_text("showfetch --source jaweed3", 2, t.curr_col + 1, True, speed=0.1)

identity = (
    "\x1b[96m\x1b[1mFatih Jawwad Al Mumtaz\x1b[0m\n"
    "\x1b[96m\u2500" * 40 + "\x1b[0m\n"
    "\x1b[96mRole:   \x1b[93mML Engineering Student & Developer\x1b[0m\n"
    "\x1b[96mSchool: \x1b[93mUNIDA Gontor\x1b[0m\n"
    "\x1b[96mFocus:  \x1b[93mEdge AI, ONNX, Embedded ML\x1b[0m\n"
    "\x1b[96m\u2500" * 40 + "\x1b[0m\n"
    "\x1b[96mTechnical Skills\x1b[0m\n"
    "\x1b[96mML/AI:    \x1b[0m \x1b[35mONNX\x1b[0m  \x1b[36mTract\x1b[0m  \x1b[32mBurn\x1b[0m  \x1b[34mPyTorch\x1b[0m\n"
    "\x1b[96mLanguages:\x1b[0m \x1b[31mRust\x1b[0m  \x1b[32mPython\x1b[0m  \x1b[34mGo\x1b[0m  \x1b[33mTypeScript\x1b[0m\n"
    "\x1b[96mInfra:    \x1b[0m \x1b[33mDocker\x1b[0m  \x1b[34mK8s\x1b[0m  \x1b[31mLinux\x1b[0m  \x1b[35mGit\x1b[0m\n"
    "\x1b[96mProject:  \x1b[0m \x1b[36mRescueVision\x1b[0m (Edge AI Vision)\n"
    "\x1b[96m\u2500" * 40 + "\x1b[0m"
)
t.gen_text(identity, 3)
scroll(40)

# ====================================================================
# 7. Farewell
# ====================================================================
t.gen_prompt(t.curr_row)
t.gen_typing_text('echo "thanks for stopping by!"', t.curr_row, t.curr_col + 1, True, speed=0.2)
scroll(25)
t.gen_prompt(t.curr_row)
t.gen_typing_text("poweroff", t.curr_row, t.curr_col + 1, True, speed=0.1)
scroll(5)
t.clear_frame()
t.set_txt_color("green")
t.gen_text("system halted.  (power cycle to reboot)", 1)
t.set_txt_color("white")
scroll(30)

# ====================================================================
t.gen_gif()
