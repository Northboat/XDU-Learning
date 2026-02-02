package com.jvmtest;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class GCStressTest {
    // 控制对象存活率（0.1表示10%存活）
    private static final double SURVIVAL_RATE = 0.1;
    // 每次循环创建的对象数量
    private static final int OBJECT_COUNT_PER_LOOP = 1000;
    // 存活对象的存储列表（避免被GC回收）
    private static final List<Object> survivorList = new ArrayList<>();
    private static final Random random = new Random();

    public static void main(String[] args) throws InterruptedException {
        System.out.println("GC Stress Test started. Press Ctrl+C to stop.");

        while (true) {
            // 每次循环创建一批对象
            for (int i = 0; i < OBJECT_COUNT_PER_LOOP; i++) {
                // 随机生成对象大小（1KB ~ 1MB）
                int size = 1024 + random.nextInt(1024 * 1023);
                byte[] obj = new byte[size];

                // 按存活率保留部分对象
                if (random.nextDouble() < SURVIVAL_RATE) {
                    survivorList.add(obj);
                }
            }

            // 定期清理部分存活对象（模拟对象生命周期）
            if (survivorList.size() > 10000) {
                // 移除前50%的对象
                survivorList.subList(0, survivorList.size() / 2).clear();
            }

            // 控制创建速度（调整睡眠时间可改变GC压力）
            Thread.sleep(10);
        }
    }
}

