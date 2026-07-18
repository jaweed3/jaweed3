<svg viewBox="0 0 960 280" xmlns="http://www.w3.org/2000/svg" font-family="'JetBrains Mono','Fira Code',ui-monospace,Consolas,monospace">
  <defs>
    <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="#141B22" stroke-width="1"/>
    </pattern>
    <linearGradient id="vignette" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.25"/>
    </linearGradient>
    <path id="tracePath" d="M -20 20 H 980"/>
  </defs>

  <!-- background -->
  <rect width="960" height="280" fill="#0A0E12"/>
  <rect width="960" height="280" fill="url(#grid)"/>
  <rect width="960" height="280" fill="url(#vignette)"/>

  <!-- top circuit trace -->
  <line x1="0" y1="20" x2="960" y2="20" stroke="#1B242C" stroke-width="1"/>
  <circle r="3.2" fill="#FF9F5A">
    <animateMotion dur="6s" repeatCount="indefinite">
      <mpath href="#tracePath"/>
    </animateMotion>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.9;1" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- name / role -->
  <text x="40" y="70" font-size="34" font-weight="700" letter-spacing="2" fill="#E6EDF3">JAWWAD</text>
  <text x="40" y="94" font-size="13" letter-spacing="0.5" fill="#6B7785">Edge ML &#183; Quantization &#183; Systems Optimization</text>

  <!-- boot log -->
  <text x="40" y="158" font-family="'JetBrains Mono','Fira Code',ui-monospace,Consolas,monospace" font-size="13" fill="#8CF5C6" opacity="0">
    <tspan fill="#4CFFB3">&gt;</tspan> init edge_runtime
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.72;0.78" dur="9s" begin="0.6s" repeatCount="indefinite"/>
  </text>
  <text x="40" y="178" font-family="'JetBrains Mono','Fira Code',ui-monospace,Consolas,monospace" font-size="13" fill="#8CF5C6" opacity="0">
    <tspan fill="#4CFFB3">&gt;</tspan> load yolov8n.onnx [ONNX Runtime]
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.72;0.78" dur="9s" begin="1.7s" repeatCount="indefinite"/>
  </text>
  <text x="40" y="198" font-family="'JetBrains Mono','Fira Code',ui-monospace,Consolas,monospace" font-size="13" fill="#8CF5C6" opacity="0">
    <tspan fill="#4CFFB3">&gt;</tspan> quantize fp32 -> int8
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.72;0.78" dur="9s" begin="2.8s" repeatCount="indefinite"/>
  </text>
  <text x="40" y="218" font-family="'JetBrains Mono','Fira Code',ui-monospace,Consolas,monospace" font-size="13" fill="#8CF5C6" opacity="0">
    <tspan fill="#4CFFB3">&gt;</tspan> deploy: no cloud, no excuses
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.05;0.72;0.78" dur="9s" begin="3.9s" repeatCount="indefinite"/>
  </text>

  <text x="40" y="238" font-size="13" fill="#4CFFB3" opacity="0">
    <tspan>$ status: READY</tspan>
    <animate attributeName="opacity" values="0;1;1;1" keyTimes="0;0.05;0.5;1" dur="9s" begin="5.3s" repeatCount="indefinite"/>
  </text>
  <rect x="163" y="227" width="8" height="13" fill="#4CFFB3" opacity="0">
    <animate attributeName="opacity" values="0;1;1;1;0;0" keyTimes="0;0.05;0.15;0.85;0.9;1" dur="9s" begin="5.3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0;1" dur="1s" begin="5.8s" repeatCount="indefinite"/>
  </rect>

  <!-- quantization scope panel -->
  <rect x="508" y="40" width="412" height="196" rx="4" fill="#10161C" stroke="#1B242C" stroke-width="1"/>
  <text x="520" y="58" font-size="11" letter-spacing="1.5" fill="#6B7785">QUANTIZATION SCOPE</text>

  <text x="520" y="106" font-size="10" fill="#4CFFB3" opacity="0.8">FP32</text>
  <rect x="528.0" width="25.5" y="104.6" height="15.4" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="15.4;33.4;12.6;29.3;15.4" dur="2.06s" begin="0.0s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="104.6;86.6;107.4;90.7;104.6" dur="2.06s" begin="0.0s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="559.5" width="25.5" y="107.9" height="12.1" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="12.1;28.3;11.3;25.6;12.1" dur="2.09s" begin="0.11s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="107.9;91.7;108.7;94.4;107.9" dur="2.09s" begin="0.11s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="591.0" width="25.5" y="106.7" height="13.3" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="13.3;25.3;39.8;14.5;13.3" dur="1.86s" begin="0.22s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="106.7;94.7;80.2;105.5;106.7" dur="1.86s" begin="0.22s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="622.5" width="25.5" y="87.4" height="32.6" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="32.6;44.1;30.8;24.3;32.6" dur="1.98s" begin="0.33s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="87.4;75.9;89.2;95.7;87.4" dur="1.98s" begin="0.33s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="654.0" width="25.5" y="108.3" height="11.7" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="11.7;40.9;20.4;15.2;11.7" dur="2.58s" begin="0.44s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="108.3;79.1;99.6;104.8;108.3" dur="2.58s" begin="0.44s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="685.5" width="25.5" y="98.9" height="21.1" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="21.1;39.4;16.5;30.9;21.1" dur="1.89s" begin="0.55s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="98.9;80.6;103.5;89.1;98.9" dur="1.89s" begin="0.55s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="717.0" width="25.5" y="96.6" height="23.4" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="23.4;29.7;12.3;12.1;23.4" dur="2.31s" begin="0.66s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="96.6;90.3;107.7;107.9;96.6" dur="2.31s" begin="0.66s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="748.5" width="25.5" y="85.5" height="34.5" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="34.5;25.4;21.3;31.1;34.5" dur="1.96s" begin="0.77s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="85.5;94.6;98.7;88.9;85.5" dur="1.96s" begin="0.77s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="780.0" width="25.5" y="99.2" height="20.8" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="20.8;38.6;35.2;18.8;20.8" dur="2.16s" begin="0.88s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="99.2;81.4;84.8;101.2;99.2" dur="2.16s" begin="0.88s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="811.5" width="25.5" y="91.1" height="28.9" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="28.9;41.5;36.3;20.4;28.9" dur="2.26s" begin="0.99s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="91.1;78.5;83.7;99.6;91.1" dur="2.26s" begin="0.99s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="843.0" width="25.5" y="105.7" height="14.3" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="14.3;25.1;37.3;15.5;14.3" dur="2.58s" begin="1.1s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="105.7;94.9;82.7;104.5;105.7" dur="2.58s" begin="1.1s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <rect x="874.5" width="25.5" y="108.6" height="11.4" rx="1.5" fill="#4CFFB3" fill-opacity="0.85">
    <animate attributeName="height" values="11.4;34.1;37.5;30.6;11.4" dur="2.19s" begin="1.21s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
    <animate attributeName="y" values="108.6;85.9;82.5;89.4;108.6" dur="2.19s" begin="1.21s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1;0.4 0 0.6 1" keyTimes="0;0.33;0.66;1"/>
  </rect>
  <line x1="520" y1="128" x2="908" y2="128" stroke="#1B242C" stroke-width="1" stroke-dasharray="2 3"/>

  <text x="520" y="146" font-size="10" fill="#FF9F5A" opacity="0.9">INT8</text>
  <rect x="528.0" width="25.5" y="184" height="30" rx="1.5" fill="#FF9F5A"/>
  <rect x="559.5" width="25.5" y="174" height="40" rx="1.5" fill="#FF9F5A"/>
  <rect x="591.0" width="25.5" y="194" height="20" rx="1.5" fill="#FF9F5A"/>
  <rect x="622.5" width="25.5" y="204" height="10" rx="1.5" fill="#FF9F5A"/>
  <rect x="654.0" width="25.5" y="174" height="40" rx="1.5" fill="#FF9F5A"/>
  <rect x="685.5" width="25.5" y="184" height="30" rx="1.5" fill="#FF9F5A"/>
  <rect x="717.0" width="25.5" y="204" height="10" rx="1.5" fill="#FF9F5A"/>
  <rect x="748.5" width="25.5" y="194" height="20" rx="1.5" fill="#FF9F5A"/>
  <rect x="780.0" width="25.5" y="174" height="40" rx="1.5" fill="#FF9F5A"/>
  <rect x="811.5" width="25.5" y="184" height="30" rx="1.5" fill="#FF9F5A"/>
  <rect x="843.0" width="25.5" y="194" height="20" rx="1.5" fill="#FF9F5A"/>
  <rect x="874.5" width="25.5" y="204" height="10" rx="1.5" fill="#FF9F5A"/>

  <text x="520" y="228" font-size="12" fill="#E6EDF3">~90% smaller <tspan fill="#6B7785">&#183;</tspan> &lt;40ms latency</text>

  <!-- footer -->
  <line x1="40" y1="252" x2="920" y2="252" stroke="#1B242C" stroke-width="1"/>
  <text x="40" y="270" font-size="11" fill="#6B7785">UNIDA Gontor, Indonesia</text>
  <text x="920" y="270" font-size="11" fill="#6B7785" text-anchor="end">Erasmus+ KA171 &#183; Univ. of Seville</text>
</svg>
