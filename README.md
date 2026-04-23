<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXN4YWxkZGNleGx5MWJqMmJ1bWFjY200b3MxOHJ5cm5xdnI3d3J0cyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/LPFNd1AJBoYcVUExmE/giphy.gif"/>
</p>

```cpp
/**
 * @file    README.md
 * @author  Jawwad
 * @brief   Computer Engineer. Edge ML. Systems Optimization.
 *          Indonesia · UNIDA Gontor · Erasmus+ KA171 Scholar @ Univ. of Seville
 */

#include <edge_ai.h>
#include <ambition.h>
#include <no_excuses.h>

struct Engineer {
    const char* name        = "Jawwad";
    const char* focus       = "Edge ML · Quantization · MLOps";
    const char* location    = "Indonesia — currently Seville, Spain";
    const char* target      = "NAIST (Robotics) via MEXT · GSoC 2026";

    constexpr bool cloud_required() const { return false; }
};

map<Domain, vector<Skill>> stack = {
    { ML_INFERENCE,   { "PyTorch", "ONNX", "OpenVINO", "TFLite", "YOLOv8" } },
    { EDGE_HARDWARE,  { "ESP32-S3", "ARM Cortex", "Apple M4"               } },
    { SYSTEMS,        { "C++", "Python", "Bash"                             } },
    { MLOPS,          { "FastAPI", "Docker", "MLflow", "DVC"               } },
    { ENVIRONMENT,    { "Arch Linux", "macOS", "Neovim", "Hyprland"        } },
};

void ask_me_about() {
    quantization();        // INT8, zero-point folding, fake-quant graphs
    graph_optimization();  // OpenVINO graph_optimizer, ACL executor wiring
    edge_deployment();     // sub-10ms inference, no cloud, no excuses
}

Project projects[] = {
    {
        .name   = "RescueVision Edge",
        .desc   = "SAR victim detection on drone imagery. "
                  "YOLOv8n ONNX, fully on-device, <40ms latency.",
        .stack  = { "YOLOv8n", "ONNX Runtime", "FastAPI", "DJI EXIF GPS" },
        .status = SUBMITTED,   // FindIT! 2026 Hackathon — Track A: Edge Vision
    },
    {
        .name   = "OpenVINO ARM INT8",
        .desc   = "INT8 convolution optimization for ARM via ACL. "
                  "Deep in graph_optimizer.cpp.",
        .stack  = { "C++", "OpenVINO", "ARM Compute Library" },
        .status = IN_PROGRESS,
    },
    {
        .name   = "BitJETS-M4",
        .desc   = "1.58-bit TTS on Apple Silicon. "
                  "Ternary weights {-1,0,1}, ~90% size reduction vs FP32.",
        .stack  = { "PyTorch", "BitNet b1.58", "MPS", "HiFi-GAN" },
        .status = RESEARCH_PREVIEW,
    },
    {
        .name   = "PerpusGate",
        .desc   = "Library access system with face recognition. Running in production.",
        .stack  = { "InsightFace", "FastAPI", "MySQL", "Vanilla JS" },
        .status = PRODUCTION,
    },
};

int main() {
    Engineer me;
    assert(!me.cloud_required());

    while (alive) {
        ship(projects);
        optimize(stack[ML_INFERENCE]);
        ignore(noise);
    }
}
```
