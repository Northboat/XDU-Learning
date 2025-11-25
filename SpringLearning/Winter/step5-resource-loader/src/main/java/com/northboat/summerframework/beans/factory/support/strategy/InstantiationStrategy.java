package com.northboat.summerframework.beans.factory.support.strategy;

import com.northboat.summerframework.beans.BeansException;
import com.northboat.summerframework.beans.factory.config.BeanDefinition;

import java.lang.reflect.Constructor;

// 实例化策略接口
public interface InstantiationStrategy {

    // 初始化 Bean
    Object instantiate(BeanDefinition beanDefinition, String beanName, Constructor<?> ctor, Object[] args) throws BeansException;
}
