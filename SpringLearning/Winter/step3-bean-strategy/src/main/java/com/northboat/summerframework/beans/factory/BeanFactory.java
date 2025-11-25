package com.northboat.summerframework.beans.factory;


import com.northboat.summerframework.beans.BeansException;

public interface BeanFactory {

    public Object getBean(String beanName) throws BeansException;

    // 传递构造函数入参获取实例对象
    public Object getBean(String beanName, Object... args) throws BeansException;
}
