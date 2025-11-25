package com.northboat.summerframework.test;

import com.northboat.summerframework.beans.factory.config.BeanDefinition;
import com.northboat.summerframework.beans.factory.support.DefaultListableBeanFactory;
import com.northboat.summerframework.test.bean.UserService;
import org.junit.jupiter.api.Test;

public class ApiTest {

    @Test
    public void testBeanFactory(){

        DefaultListableBeanFactory beanFactory = new DefaultListableBeanFactory();

        // 通过 class 注册 Bean
        BeanDefinition userServiceBean = new BeanDefinition(UserService.class);
        beanFactory.registerBeanDefinition("userService", userServiceBean);

        // 获取 Bean
        // 第一次没有实例化，会调用 createBean
        UserService userService = (UserService) beanFactory.getBean("userService", "northboat");
        userService.queryUserInfo();
    }

}
