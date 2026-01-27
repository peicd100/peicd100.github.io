假設 $L_m=$ (你可以更改以下數字)
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .input-container {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input[type="number"] {
            background-color: transparent;
            border: none;
            border-bottom: 2px solid #F2BBFF;
            font-size: 18px;
            padding: 5px;
            width: 60px;
            text-align: center;
            outline: none;
        }

        input[type="number"]:focus {
            border-bottom-color: #F2BBFF;
        }


        #chart-container {
            width: 80%;
            max-width: 600px;
            margin: 20px auto;
            background-color: white; /* 設置圖表容器背景為白色 */
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        #output {
            font-size: 18px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="input-container">
        <p>[</p>
        <input type="number" id="num1" value="1">
        <p>,</p>
        <input type="number" id="num2" value="2">
        <p>,</p>
        <input type="number" id="num3" value="5">
        <p>,</p>
        <input type="number" id="num4" value="3">
        <p>,</p>
        <input type="number" id="num5" value="4">
        <p>]</p>
    </div>

    <!-- 圖表容器 -->
    <div id="chart-container">
        <canvas id="probabilityChart"></canvas>
    </div>

    <!-- 計算過程輸出 -->
    <p id="output"></p>

    <script>
        let chart; // 用於存儲圖表實例

        // Softmax 計算函數
        function calculateSoftmax() {
            const outputDiv = document.getElementById('output');
            outputDiv.innerHTML = ''; // 清空結果
            
            // 獲取輸入數值
            const inputs = [
                parseFloat(document.getElementById('num1').value),
                parseFloat(document.getElementById('num2').value),
                parseFloat(document.getElementById('num3').value),
                parseFloat(document.getElementById('num4').value),
                parseFloat(document.getElementById('num5').value)
            ];

            // 確保所有輸入是有效數字
            if (inputs.some(isNaN)) {
                outputDiv.textContent = '請確保所有輸入都是有效的數字。';
                return;
            }

            // 計算 Softmax 步驟
            let resultText = "";
            resultText += `原始數字：Lm=[x1,x2,...,xn]\n[${inputs.join(', ')}]\n\n`;

            // 最大值
            const maxVal = Math.max(...inputs);
            resultText += `最大值：m\n ${maxVal}\n\n`;

            // 減去最大值
            const subtracted = inputs.map(num => num - maxVal);
            resultText += `減去最大值：xi-m\n [${subtracted.join(', ')}]\n\n`;

            // 指數函數
            const expValues = subtracted.map(num => Math.exp(num));
            resultText += `計算指數函數：e^(xi):\n [${expValues.join(', ')}]\n\n`;

            // 總和
            const sumExp = expValues.reduce((a, b) => a + b, 0);
            resultText += `指數值總和：Σ(e^(xj):\n ${sumExp}\n\n`;

            // Softmax 值
            const softmaxValues = expValues.map(num => num / sumExp);
            resultText += `Softmax 值：e^(xi)/Σ(e^(xj)\n [${softmaxValues.join(', ')}]\n\n`;

            // 總和檢查
            const total = softmaxValues.reduce((a, b) => a + b, 0);
            resultText += `Softmax 總和 (應接近 1):\n ${total}\n\n`;

            outputDiv.innerHTML = resultText.replace(/\n/g, "<br>");

            // 繪製機率分布圖
            drawChart(softmaxValues);
        }

        // 繪製長條圖
        function drawChart(data) {
            const ctx = document.getElementById('probabilityChart').getContext('2d');
            
            // 如果圖表已經存在，先銷毀再重建
            if (chart) {
                chart.destroy();
            }

            chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['x1', 'x2', 'x3', 'x4', 'x5'], // 標籤
                    datasets: [{
                        label: 'Softmax 機率分布',
                        data: data, // Softmax 值
                        backgroundColor: 'rgba(75, 192, 192, 0.6)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 1 // 確保機率分布在 [0, 1] 範圍內
                        }
                    }
                }
            });
        }

        // 監聽輸入框的變化
        document.querySelectorAll('.input-container input').forEach(input => {
            input.addEventListener('input', calculateSoftmax);
        });

        // 頁面加載時自動計算
        window.addEventListener('DOMContentLoaded', calculateSoftmax);
    </script>
</body>
</html>
(內容消失時請重新整理或按下f5)