# Jawwad

Студент компьютерной инженерии. Пишу на C++, Python. Занимаюсь квантизацией моделей и развёртыванием на граничных устройствах — там, где облако недоступно, а каждая миллисекунда на счету.

Не ищу одобрения. Ищу задачи, которые большинство сочтёт невозможными.

---

## Стек

```
struct Engineer {
    const char* name = "Jawwad";

    map<Domain, vector<Skill>> stack = {
        { ML_INFERENCE,   { "PyTorch", "ONNX", "OpenVINO", "TFLite", "YOLOv8" } },
        { EDGE_HARDWARE,  { "ESP32-S3", "ARM Cortex", "Apple M4"               } },
        { SYSTEMS,        { "C++", "Python", "Bash"                             } },
        { MLOPS,          { "FastAPI", "Docker", "MLflow"                       } },
        { ENVIRONMENT,    { "Arch Linux", "macOS", "Neovim"                     } },
    };

    void ask_me_about() {
        quantization();        // INT8, zero-point folding, fake-quant graphs
        graph_optimization();  // OpenVINO graph_optimizer, ACL executor wiring
        edge_deployment();     // sub-10ms inference, no cloud, no excuses
    }
};
```

---

## Проекты

**RescueVision Edge** — детекция пострадавших на дронах SAR. YOLOv8n, полностью на устройстве. Без облака.

**OpenVINO ARM INT8** — оптимизация INT8-свёрток для ARM через ACL. GSoC 2026. Глубоко в `graph_optimizer.cpp`. Ещё не закончено — и это честно.

**PerpusGate** — система входа в библиотеку с распознаванием лиц. InsightFace, FastAPI, MySQL. Работает в продакшене.

---

*Модели должны работать там, где нет интернета.*
