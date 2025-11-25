package com.northboat.summerframework.test;

import com.northboat.summerframework.beans.factory.config.BeanDefinition;
import com.northboat.summerframework.beans.factory.support.property.BeanReference;
import com.northboat.summerframework.beans.factory.support.DefaultListableBeanFactory;
import com.northboat.summerframework.beans.factory.support.property.PropertyValue;
import com.northboat.summerframework.beans.factory.support.property.PropertyValues;
import com.northboat.summerframework.test.bean.UserDao;
import com.northboat.summerframework.test.bean.UserService;
import org.junit.jupiter.api.Test;

public class ApiTest {

    @Test
    public void testBeanFactory(){

        DefaultListableBeanFactory beanFactory = new DefaultListableBeanFactory();

        // 注册 UserDao
        beanFactory.registerBeanDefinition("userDao", new BeanDefinition(UserDao.class));

        // 设置内置属性 uId 和 userDao
        PropertyValues propertyValues = new PropertyValues();
        propertyValues.addPropertyValue(new PropertyValue("uId", "10001"));
        propertyValues.addPropertyValue(new PropertyValue("userDao", new BeanReference("userDao")));

        // 注册 UserService 并将内置属性注入
        BeanDefinition userServiceBean = new BeanDefinition(UserService.class, propertyValues);
        beanFactory.registerBeanDefinition("userService", userServiceBean);

        // 获取 UserService Bean
        UserService userService = (UserService) beanFactory.getBean("userService");
        userService.queryUserInfo();
    }

}
