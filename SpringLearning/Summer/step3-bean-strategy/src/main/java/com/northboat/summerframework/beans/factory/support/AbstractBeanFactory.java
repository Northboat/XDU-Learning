package com.northboat.summerframework.beans.factory.support;

import com.northboat.summerframework.beans.BeansException;
import com.northboat.summerframework.beans.factory.BeanFactory;
import com.northboat.summerframework.beans.factory.config.BeanDefinition;
import com.northboat.summerframework.beans.factory.support.singleton.DefaultSingletonBeanRegistry;

public abstract class AbstractBeanFactory extends DefaultSingletonBeanRegistry implements BeanFactory {

    // 实现 BeanFactory 的 getBean 接口
    @Override
    public Object getBean(String beanName){
        return doGetBean(beanName);
    }

    @Override
    public Object getBean(String beanName, Object... args) throws BeansException {
        return doGetBean(beanName, args);
    }


    protected <T> T doGetBean(String beanName, Object... args) throws BeansException {
        Object bean = getSingleton(beanName);
        if(bean != null){
            return (T) bean;
        }

        // 当 Bean Object 并未初始化，使用 Class 对象进行实例化
        BeanDefinition beanDefinition = getBeanDefinition(beanName);
        return (T) createBean(beanName, beanDefinition, args);
    }

    // 获取 Bean Class 实例，用于创建 Bean Object
    protected abstract BeanDefinition getBeanDefinition(String beanName) throws BeansException;

    // 根据入参 args 创建 Object 并存入单例的 Map 中
    protected abstract Object createBean(String beanName, BeanDefinition beanDefinition, Object... args) throws BeansException;
}
