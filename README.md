```
/**
 * @file    README.md
 * @author  Jawwad
 * @brief   Компьютерный инженер. Edge ML. Системная оптимизация.
 *          Индонезия · UNIDA Gontor · Sem. 5
 */

#include <edge_ai.h>
#include <ambition.h>
#include <no_excuses.h>

struct Engineer {
    const char* name        = "Jawwad";
    const char* focus       = "Edge ML · Quantization · MLOps";
    const char* location    = "Ponorogo, Indonesia";
    const char* target      = "NAIST (Robotics) via MEXT · GSoC 2026";

    constexpr bool cloud_required() const { return false; }
};

map<Domain, vector<Skill>> stack = {
    { ML_INFERENCE,   { "PyTorch", "ONNX", "OpenVINO", "TFLite", "YOLOv8" } },
    { EDGE_HARDWARE,  { "ESP32-S3", "ARM Cortex", "Apple M4"               } },
    { SYSTEMS,        { "C++", "Python", "Bash"                             } },
    { MLOPS,          { "FastAPI", "Docker", "MLflow"                       } },
    { ENVIRONMENT,    { "Arch Linux", "macOS", "Neovim", "Hyprland"        } },
};

void ask_me_about() {
    quantization();        // INT8, zero-point folding, fake-quant graphs
    graph_optimization();  // OpenVINO graph_optimizer, ACL executor wiring
    edge_deployment();     // sub-10ms inference, no cloud
}

Project projects[] = {
    {
        .name   = "RescueVision Edge",
        .desc   = "Детекция пострадавших на дронах SAR. "
                  "YOLOv8n, полностью на устройстве.",
        .stack  = { "YOLOv8n", "ESP32-S3", "FastAPI", "DJI EXIF GPS" },
        .status = SUBMITTED, 
    },
    {
        .name   = "OpenVINO ARM INT8",
        .desc   = "Оптимизация INT8-свёрток для ARM через ACL. "
                  "Глубоко в graph_optimizer.cpp.",
        .stack  = { "C++", "OpenVINO", "ARM Compute Library" },
        .status = IN_PROGRESS, 
    },
    {
        .name   = "PerpusGate",
        .desc   = "Система входа в библиотеку с распознаванием лиц. "
                  "Работает в продакшене.",
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
