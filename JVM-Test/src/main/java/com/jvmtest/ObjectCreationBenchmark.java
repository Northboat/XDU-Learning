package com.jvmtest;

import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

// 测试模式：吞吐量（每秒操作数）
@BenchmarkMode(Mode.Throughput)
// 结果输出单位：秒
@OutputTimeUnit(TimeUnit.SECONDS)
// 预热次数：3次（让JIT编译稳定）
@Warmup(iterations = 3, time = 1, timeUnit = TimeUnit.SECONDS)
// 测量次数：5次（取平均值）
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
// 线程数：1（单线程测试，避免线程干扰）
@Threads(1)
// 状态对象：每个线程一个实例
@State(Scope.Thread)
public class ObjectCreationBenchmark {

    // 测试：创建普通对象
    @Benchmark
    public Object testPlainObject() {
        return new Object();
    }

    // 测试：创建小对象（1KB）
    @Benchmark
    public byte[] testSmallObject() {
        return new byte[1024]; // 1KB
    }

    // 测试：创建中对象（100KB）
    @Benchmark
    public byte[] testMediumObject() {
        return new byte[1024 * 100]; // 100KB
    }

    // 主方法：启动JMH测试
    public static void main(String[] args) throws Exception {
        org.openjdk.jmh.Main.main(args);
    }
}
