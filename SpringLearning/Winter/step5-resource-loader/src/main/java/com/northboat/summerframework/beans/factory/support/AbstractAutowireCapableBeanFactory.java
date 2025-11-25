package com.northboat.summerframework.beans.factory.support;

import cn.hutool.core.bean.BeanUtil;
import com.northboat.summerframework.beans.BeansException;
import com.northboat.summerframework.beans.factory.config.BeanDefinition;
import com.northboat.summerframework.beans.factory.support.property.BeanReference;
import com.northboat.summerframework.beans.factory.support.property.PropertyValue;
import com.northboat.summerframework.beans.factory.support.property.PropertyValues;
import com.northboat.summerframework.beans.factory.support.strategy.CglibSubclassingInstantiationStrategy;
import com.northboat.summerframework.beans.factory.support.strategy.InstantiationStrategy;

import java.lang.reflect.Constructor;

// 实现 createBean 函数，完成 Bean 的自动注入
public abstract class AbstractAutowireCapableBeanFactory extends AbstractBeanFactory{

    private InstantiationStrategy instantiationStrategy = new CglibSubclassingInstantiationStrategy();
//    private InstantiationStrategy instantiationStrategy = new SimpleInstantiationStrategy();

    // 一个 BeanDefinition 包括这个 Bean 对应的 Class 类和其内部属性列表
    // 若内部属性也为 Bean，那么将在属性列表中标注为 BeanReference，BeanReference 中将存放这个 Bean 的名称，作为 getBean 的入参以获取实例对象
    @Override
    protected Object createBean(String beanName, BeanDefinition beanDefinition, Object[] args) throws BeansException {
        Object bean = null;
        try {
            // 创建实例
            bean = createBeanInstance(beanDefinition, beanName, args);
            // 填充属性
            applyPropertyValues(beanName, bean, beanDefinition);
        } catch (Exception e) {
            throw new BeansException("Instantiation of bean failed", e);
        }

        addSingleton(beanName, bean);
        return bean;
    }

    protected Object createBeanInstance(BeanDefinition beanDefinition, String beanName, Object[] args) {
        Constructor<?> constructor = null;
        Class<?> beanClass = beanDefinition.getBeanClass();
        // 获取 Class 类的构造函数们
        Constructor<?>[] declaredConstructors = beanClass.getDeclaredConstructors();
        // 遍历构造函数，找到入参长度相同的构造函数
        for(Constructor<?> ctor: declaredConstructors){
            if(args != null && ctor.getParameterTypes().length == args.length){
                constructor = ctor;
                break;
            }
        }
        return getInstantiationStrategy().instantiate(beanDefinition, beanName, constructor, args);
    }

    public InstantiationStrategy getInstantiationStrategy() {
        return instantiationStrategy;
    }

    public void setInstantiationStrategy(InstantiationStrategy instantiationStrategy) {
        this.instantiationStrategy = instantiationStrategy;
    }

    // Bean 属性填充
    protected void applyPropertyValues(String beanName, Object bean, BeanDefinition beanDefinition) {
        try{
            PropertyValues propertyValues = beanDefinition.getPropertyValues();
            for(PropertyValue propertyValue: propertyValues.getPropertyValues()){
                String name = propertyValue.name();
                Object value = propertyValue.value();

                // 没看懂这里，这里只是一个简单的模拟
                // 就是说，如果当前的属性是 beanReference 的一个引用，说明这个属性也是一个 Bean
                // 那么就直接从 Map 中 getBean 以获取这个 Bean 的实例化对象
                if(value instanceof BeanReference beanReference){
                    // 如果 A 依赖于 B，获取 B 的实例化
                    value = getBean(beanReference.beanName());
                }
                BeanUtil.setFieldValue(bean, name, value);
            }
        }catch (Exception e){
            throw new BeansException("Error setting property values: " + beanName);
        }
    }

}
