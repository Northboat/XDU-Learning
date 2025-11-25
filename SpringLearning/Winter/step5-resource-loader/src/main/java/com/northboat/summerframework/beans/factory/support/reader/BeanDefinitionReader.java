package com.northboat.summerframework.beans.factory.support.reader;

import com.northboat.summerframework.beans.BeansException;
import com.northboat.summerframework.beans.factory.config.BeanDefinitionRegistry;
import com.northboat.summerframework.core.io.Resource;
import com.northboat.summerframework.core.io.ResourceLoader;

public interface BeanDefinitionReader {

    BeanDefinitionRegistry getRegistry();

    ResourceLoader getResourceLoader();

    void loadBeanDefinitions(Resource resource) throws BeansException;

    void loadBeanDefinitions(Resource... resource) throws BeansException;

    void loadBeanDefinitions(String location) throws BeansException;
}
