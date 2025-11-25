package com.northboat.summerframework;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class BeanFactory {

    // 防止并发错误使用线程安全的 ConcurrentHashMap
    private final Map<String, BeanDefinition> beanDefinitionMap = new ConcurrentHashMap<>();

    // 获取单例的 Bean 对象
    public Object getBean(String beanName) {
        return beanDefinitionMap.get(beanName).bean();
    }

    // Bean 的注册
    public void registerBeanDefinition(String beanName, BeanDefinition beanDefinition) {
        beanDefinitionMap.put(beanName, beanDefinition);
    }
}
