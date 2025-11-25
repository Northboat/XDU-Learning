package com.northboat.summerframework.test;

import com.northboat.summerframework.BeanDefinition;
import com.northboat.summerframework.BeanFactory;
import com.northboat.summerframework.test.bean.UserService;
import org.junit.jupiter.api.Test;

public class ApiTest {

    @Test
    public void testBeanFactory(){
        // 初始化工厂
        BeanFactory beanFactory = new BeanFactory();

        // 注册 Bean
        BeanDefinition beanDefinition = new BeanDefinition(new UserService());
        beanFactory.registerBeanDefinition("userService", beanDefinition);

        // 获取并使用 Bean
        UserService userService = (UserService) beanFactory.getBean("userService");
        userService.queryUserInfo();
    }


    @Test
    public void testBeanFactory2(){
        BeanFactory beanFactory = new BeanFactory();
        System.out.println("nmsl");
    }

}
