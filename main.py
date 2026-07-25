import gifos

USERNAME = "jaweed3"

t = gifos.Terminal(width=680, height=600, xpad=5, ypad=5, font_size=15)
t.set_fps(15)


def boot_line(text, row, delay=2, color="white", contin=False):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    t.set_txt_color("white")


def progress_bar(pct, width=20):
    fill = int(pct / 100 * width)
    bar = "\x1b[32m" + "#" * fill + "\x1b[90m" + "." * (width - fill) + "\x1b[0m"
    return f"[{bar}] {pct:3d}%"


def progress_animate(text, row, delay_fn=None, inverted=False):
    start, end, step = (100, 0, -5) if inverted else (0, 101, 5)
    for pct in range(start, end, step):
        if delay_fn:
            d = delay_fn(pct, start, end)
        else:
            d = 1
        t.delete_row(row)
        bar = progress_bar(pct) if not inverted else progress_bar(100 - pct)
        t.gen_text(f"  {bar}  {text}", row)
        t.clone_frame(d)


# --- 1. ML Runtime Init ---------------------------------------------
boot_line(f"{USERNAME} ML Runtime v0.4.2", 1, delay=5)
boot_line("  [OK] ONNX Runtime 1.21.0", 2, delay=3, color="green")
boot_line("  [OK] CUDA 12.8 detected", 3, delay=2, color="green")
boot_line("  [OK] TensorRT 10.7", 4, delay=2, color="green")

t.gen_text("  loading runtime kernels...", 5)
for speed in range(20, 101, 10):
    t.delete_row(5)
    t.gen_text(f"  loading runtime kernels... {speed}%", 5)
    t.clone_frame(1)
t.delete_row(5)
boot_line("  loading runtime kernels...", 5, delay=1, color="green", contin=True)
boot_line(" done", 5, delay=1, color="green", contin=True)

t.clone_frame(10)
progress_animate("initializing compute graph", 7)
t.clone_frame(5)
t.clear_frame()

# --- 2. Model Load --------------------------------------------------
boot_line("model ingest: rescuevision.onnx", 1, delay=3)
boot_line("  architecture: YOLOv8n-seg", 2, delay=2, color="cyan")
boot_line("  input:  3x224x224  (RGB)", 3, delay=2)
boot_line("  params: 3.27M", 4, delay=2)

# model summary table
summary = (
    "\x1b[90m  layer            out shape      params\x1b[0m\n"
    "\x1b[90m  \x1b[0m conv1      64x112x112      1,856\n"
    "\x1b[90m  \x1b[0m conv2     128x56x56       73,856\n"
    "\x1b[90m  \x1b[0m c2f_1     128x56x56      197,632\n"
    "\x1b[90m  \x1b[0m conv3     256x28x28      295,424\n"
    "\x1b[90m  \x1b[0m c2f_2     256x28x28      591,872\n"
    "\x1b[90m  \x1b[0m conv4     512x14x14      590,336\n"
    "\x1b[90m  \x1b[0m c2f_3     512x14x14      591,872\n"
    "\x1b[90m  \x1b[0m spp       512x14x14      262,400\n"
    "\x1b[90m  \x1b[0m detekt    (84+32)x8400    55,296\n"
    "\x1b[90m  \x1b[0m \x1b[33m------------------------------\x1b[0m\n"
    "\x1b[90m  \x1b[0m total                   3,267,392"
)
t.gen_text(summary, 5)

t.gen_text("  compiling graph...", 14)
for speed in range(5, 105, 5):
    t.delete_row(14)
    t.gen_text(f"  compiling graph... {speed}%", 14)
    t.clone_frame(1)
t.delete_row(14)
boot_line("  compiling graph...", 14, delay=1, color="green", contin=True)
boot_line(" done", 14, delay=1, color="green", contin=True)

t.clone_frame(15)
t.clear_frame()

# -- 3. Quantization ------------------------------------------------
boot_line("quantization: FP32 -> INT8", 1, delay=3)

t.gen_text("  calibrating on 512 samples...", 2)
t.clone_frame(5)

for pct in range(0, 101, 10):
    t.delete_row(3)
    t.gen_text(f"  {progress_bar(pct, 30)}  layer {pct//10 + 1}/10", 3)
    t.clone_frame(2)

t.clone_frame(5)
boot_line("  model size: 12.47 MB  ->  \x1b[33m3.12 MB\x1b[0m", 4, delay=4, contin=True)
boot_line("  latency:    42.1 ms  ->  \x1b[33m21.8 ms\x1b[0m  (\x1b[32m-48%\x1b[0m)", 5, delay=4)
boot_line("  accuracy:   0.893   ->  \x1b[33m0.882\x1b[0m  (\x1b[32m-1.2%\x1b[0m)", 6, delay=4)
t.clone_frame(10)
boot_line("  \x1b[32moptimization profile: edge_server_fast\x1b[0m", 7, delay=3)
t.clone_frame(15)
t.clear_frame()

# -- 4. Deploy to Edge ----------------------------------------------
t.gen_text("                     \x1b[96m\x1b[1m  DEPLOY TARGET\x1b[0m", row_num=1)
t.gen_text("  \x1b[90m  +-----------------------------------------+\x1b[0m", row_num=2)
t.gen_text("  \x1b[90m  |\x1b[0m  device:   \x1b[93mRescueVision v2 @ RPi 5\x1b[0m     \x1b[90m|\x1b[0m", row_num=3)
t.gen_text("  \x1b[90m  |\x1b[0m  status:   \x1b[32mconnecting...\x1b[0m              \x1b[90m|\x1b[0m", row_num=4)
t.gen_text("  \x1b[90m  |\x1b[0m  protocol: \x1b[35mUSB-C / MIPI CSI\x1b[0m          \x1b[90m|\x1b[0m", row_num=5)
t.gen_text("  \x1b[90m  |\x1b[0m  power:    5V 3A (15W)                \x1b[90m|\x1b[0m", row_num=6)
t.gen_text("  \x1b[90m  +-----------------------------------------+\x1b[0m", row_num=7)
t.clone_frame(10)

for pct in range(0, 101, 5):
    t.delete_row(4)
    label = "connected" if pct >= 20 else "connecting..."
    status_color = "\x1b[32m" if pct >= 100 else "\x1b[93m" if pct >= 20 else "\x1b[90m"
    t.gen_text(f"  \x1b[90m  |\x1b[0m  status:   {status_color}{label}\x1b[0m{' ' * (20 - len(label))}\x1b[90m|\x1b[0m", 4)
    t.clone_frame(1)

t.delete_row(4)
t.gen_text("  \x1b[90m  |\x1b[0m  status:   \x1b[32mconnected\x1b[0m                  \x1b[90m|\x1b[0m", 4)
t.clone_frame(5)

# deploying progress
for pct in range(0, 101, 2):
    t.delete_row(9)
    t.gen_text(f"     deploying model {progress_bar(pct, 25)}", 9)
    t.clone_frame(1)

t.clone_frame(5)
t.gen_text("  \x1b[32m  inference pipeline ACTIVE  @  30 FPS\x1b[0m", 10)
t.clone_frame(15)
t.clear_frame()

# -- 5. Login -------------------------------------------------------
t.gen_text(text="\x1b[32mjaweed3\x1b[0m login: ", row_num=1)
t.gen_typing_text(text="jaweed3", row_num=1, col_num=17, contin=True, speed=0.1)
t.clone_frame(10)
t.gen_text(text="Password: ", row_num=2)
t.gen_typing_text(text="********", row_num=2, col_num=11, contin=True, speed=0.1)
t.clone_frame(15)
t.clear_frame()

# -- 6. Welcome + showfetch -----------------------------------------
t.gen_text(text="Welcome, Fatih!  Last login:  Sun Jul 26 00:00:01 WIB 2026", row_num=1)
t.set_prompt(f"\x1b[35m{USERNAME}\x1b[39m@\x1b[32mgithub\x1b[39m:~$ ")
t.gen_prompt(2)
t.gen_typing_text(text="showfetch --source jaweed3", row_num=2, contin=True, speed=0.1)

identity = """\x1b[96m\x1b[1mFatih Jawwad Al Mumtaz\x1b[0m
\x1b[96m----------------------------------------\x1b[0m
\x1b[96mRole:   \x1b[93mML Engineering Student & Developer\x1b[0m
\x1b[96mSchool: \x1b[93mUNIDA Gontor\x1b[0m
\x1b[96mFocus:  \x1b[93mEdge AI, ONNX, Embedded ML\x1b[0m
\x1b[96m----------------------------------------\x1b[0m
\x1b[96mTechnical Skills\x1b[0m
\x1b[96mML/AI:    \x1b[0m \x1b[35mONNX\x1b[0m  \x1b[36mTract\x1b[0m  \x1b[32mBurn\x1b[0m  \x1b[34mPyTorch\x1b[0m
\x1b[96mLanguages:\x1b[0m \x1b[31mRust\x1b[0m  \x1b[32mPython\x1b[0m  \x1b[34mGo\x1b[0m  \x1b[33mTypeScript\x1b[0m
\x1b[96mInfra:    \x1b[0m \x1b[33mDocker\x1b[0m  \x1b[34mK8s\x1b[0m  \x1b[31mLinux\x1b[0m  \x1b[35mGit\x1b[0m
\x1b[96mProject:  \x1b[0m \x1b[36mRescueVision\x1b[0m (Edge AI Vision)
\x1b[96m----------------------------------------\x1b[0m"""
t.gen_text(text=identity, row_num=3)

# -- 7. Farewell ----------------------------------------------------
t.gen_prompt(t.curr_row)
t.gen_typing_text(text='echo "thanks for stopping by!"', row_num=t.curr_row, contin=True, speed=0.2)
t.clone_frame(30)
t.gen_prompt(t.curr_row)
t.gen_typing_text("poweroff", t.curr_row, contin=True, speed=0.1)
t.clone_frame(5)
t.clear_frame()
boot_line("system halted.  (power cycle to reboot)", 1, delay=5)
t.clone_frame(30)

# -- 8. Generate GIF ------------------------------------------------
t.gen_gif()
