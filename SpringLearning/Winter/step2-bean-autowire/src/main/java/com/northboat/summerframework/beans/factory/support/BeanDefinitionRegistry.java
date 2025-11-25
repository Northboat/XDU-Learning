package com.northboat.summerframework.beans.factory.support;

import com.northboat.summerframework.beans.factory.config.BeanDefinition;

public interface BeanDefinitionRegistry {

    public void registerBeanDefinition(String beanName, BeanDefinition beanDefinition);
}
