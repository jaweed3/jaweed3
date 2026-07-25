import gifos

USERNAME = "jaweed3"

t = gifos.Terminal(width=680, height=540, xpad=5, ypad=5, font_size=15)
t.set_fps(15)


def boot_line(text, row, delay=2, color="white", contin=False):
    t.set_txt_color(color)
    t.gen_text(text=text, row_num=row, contin=contin)
    t.clone_frame(delay)
    t.set_txt_color("white")


def init_line(text, row):
    t.gen_text("[ ", row_num=row)
    t.set_txt_color("green")
    t.gen_text("OK", row_num=row, contin=True)
    t.set_txt_color("white")
    t.gen_text(" ] ", row_num=row, contin=True)
    t.gen_text(text=text, row_num=row, contin=True)


def print_dots_done(row, delay=2):
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(".", row, delay, contin=True)
    boot_line(" Done", row, delay, contin=True, color="green")


# ── 1. Boot ─────────────────────────────────────────────────────────
boot_line(f"{USERNAME} bios v2.4.1 initializing", 1, delay=5)
print_dots_done(1)

boot_line("Hardware detection", 3, delay=2)
print_dots_done(3)

boot_line("Hardware detected:", 4)
boot_line("  CPU: ARM Cortex-X4 @ 3.4GHz", 5, delay=2)
boot_line("  RAM: 16GiB LPDDR5X", 6, delay=2)
boot_line("  Display: 680x540 24-bit Terminal Renderer", 7, delay=2)
t.clone_frame(15)

boot_line("Beginning memory test...", 9, delay=4)
for i in range(0, 16384, 512):
    t.delete_row(9)
    t.gen_text(f"Beginning memory test... {i}KiB", 9)
t.delete_row(9)
boot_line("Beginning memory test...", 9)
boot_line(" 16384KiB OK", 9, color="green", contin=True)
t.clone_frame(15)
t.clear_frame()

# ── 2. OS animation ────────────────────────────────────────────────
t.gen_text("Initiating Boot Sequence ", 1, contin=True)
t.gen_typing_text(".....", 1, contin=True)

os_name = "JAWEED OS"
mid_row = (t.num_rows + 1) // 2
mid_col = (t.num_cols - len(os_name) + 1) // 2
effect_lines = gifos.effects.text_scramble_effect_lines(
    os_name, 3, include_special=False
)
for line in effect_lines:
    t.delete_row(mid_row + 1)
    t.gen_text(line, mid_row + 1, mid_col + 1)
t.clear_frame()

# ── 3. Kernel init ─────────────────────────────────────────────────
boot_line("jaweed3 kernel init", 1)
print_dots_done(1)
init_line("Starting system services...", 2)
init_line("Initializing ML runtime...", 3)
init_line("Loading ONNX runtime...", 4)
init_line("Mounting model registry...", 5)
init_line("Starting Edge AI daemon...", 6)
init_line("Initializing display server...", 7)
t.gen_text("Welcome to Jaweed OS!", 9)
t.clone_frame(15)
t.clear_frame()

# ── 4. Login ───────────────────────────────────────────────────────
t.gen_text(text="jaweed3 login: ", row_num=1)
t.gen_typing_text(text="jaweed3", row_num=1, col_num=16, contin=True, speed=0.1)
t.clone_frame(10)
t.gen_text(text="Password: ", row_num=2)
t.gen_typing_text(text="********", row_num=2, col_num=11, contin=True, speed=0.1)
t.clone_frame(15)
t.clear_frame()

# ── 5. Welcome + showfetch ─────────────────────────────────────────
t.gen_text(text="Welcome, Fatih! Last Login: Sun Jul 26 00:00:01 WIB 2026", row_num=1)
t.set_prompt(f"\x1b[35m{USERNAME}\x1b[39m@\x1b[32mgithub\x1b[39m:~$ ")
t.gen_prompt(2)
t.gen_typing_text(text="showfetch --source jaweed3", row_num=2, contin=True, speed=0.1)

identity = """\x1b[96m\x1b[1mFatih Jawwad Al Mumtaz\x1b[0m
\x1b[96m----------------------------------------\x1b[0m
\x1b[96mRole:   \x1b[93mML Engineering Student & Developer\x1b[0m
\x1b[96mSchool: \x1b[93mUNIDA Gontor\x1b[0m
\x1b[96mFocus:  \x1b[93mEdge AI, ONNX, Embedded ML\x1b[0m
\x1b[96m----------------------------------------\x1b[0m
\x1b[96m\x1b[1mTechnical Skills\x1b[0m
\x1b[96mML/AI:    \x1b[0m \x1b[35mONNX\x1b[0m  \x1b[36mTract\x1b[0m  \x1b[32mBurn\x1b[0m  \x1b[34mPyTorch\x1b[0m
\x1b[96mLanguages:\x1b[0m \x1b[31mRust\x1b[0m  \x1b[32mPython\x1b[0m  \x1b[34mGo\x1b[0m  \x1b[33mTypeScript\x1b[0m
\x1b[96mInfra:    \x1b[0m \x1b[33mDocker\x1b[0m  \x1b[34mK8s\x1b[0m  \x1b[31mLinux\x1b[0m  \x1b[35mGit\x1b[0m
\x1b[96mProject:  \x1b[0m \x1b[36mRescueVision\x1b[0m (Edge AI Vision)
\x1b[96m----------------------------------------\x1b[0m"""
t.gen_text(text=identity, row_num=3)

# ── 6. Farewell ────────────────────────────────────────────────────
t.gen_prompt(t.curr_row)
t.gen_typing_text(text='echo "thanks for stopping by!"', row_num=t.curr_row, contin=True, speed=0.2)
t.clone_frame(30)
t.gen_prompt(t.curr_row)
t.gen_typing_text("reboot", t.curr_row, contin=True, speed=0.1)
t.clone_frame(5)
t.clear_frame()
boot_line("System halted.", 1)
t.clone_frame(15)

# ── 7. Generate GIF ────────────────────────────────────────────────
t.gen_gif()
