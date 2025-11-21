package com.northboat.summerframework.beans.factory.config;

public class BeanDefinition {

    private Class<?> bean;

    public BeanDefinition(Class<?> bean){
        this.bean = bean;
    }

    public Class<?> getBeanClass() {
        return bean;
    }

    public void setBean(Class<?> bean) {
        this.bean = bean;
    }
}
