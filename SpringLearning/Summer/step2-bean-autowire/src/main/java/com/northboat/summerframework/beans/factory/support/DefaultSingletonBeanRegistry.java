package com.northboat.summerframework.beans.factory.support;

import com.northboat.summerframework.beans.factory.config.SingletonBeanRegistry;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class DefaultSingletonBeanRegistry implements SingletonBeanRegistry {

    // 因为这个涉及读写，我感觉还是得用 ConcurrentHashMap
    private final Map<String, Object> singletonObjects;

    public DefaultSingletonBeanRegistry() {
        this.singletonObjects = new ConcurrentHashMap<>();
    }

    @Override
    public Object getSingleton(String beanName) {
        return singletonObjects.get(beanName);
    }

    protected void addSingleton(String beanName, Object bean){
        singletonObjects.put(beanName, bean);
    }
}
