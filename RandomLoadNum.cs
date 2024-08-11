
using System;
using System.Collections.Generic;
using MtPadAdaptiveTool.Common;

namespace MtPadAdaptiveTool.Test
{
    public class RandomLoadNum
    {
        private double total = 0;
        private bool dist = true;

        private Random random = new Random();

        private Dictionary<int, double> randomNum = new(); 
        
        
        public double NextToolLoad(int axesNo){
            
            if(total >= 300 || total == 0){
                // 总步数到达临界点,切换方向
                dist = !dist;
            }
            
            var minValue = 1.00;
            var maxValue = 20.0;
            var randomNumber = minValue + (maxValue - minValue) * random.NextDouble();
            
            if(dist){
                // 正向
                total += randomNumber;
            }else{
                // 反向
                total -= 30;
                total = total < 0 ? 0: total;
            }
            
            //遍历当前刀, 根据倍率计算一个增量或者减少的值
            DataStore.AxesCurrentTool.TryGetValue(axesNo, out var axesToolLifeModel);
            if (axesToolLifeModel == null || axesToolLifeModel.Power == 0) return total;
            //加一个负载变化, 可以看到曲线的变化
            return total + axesToolLifeModel.Power - 100;
        }
        
        
        
    }
}