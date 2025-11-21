package com.northboat.summerframework.test.bean;


public class UserService {

    private String name;

    public UserService(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void queryUserInfo(){
        System.out.println(name + " is querying user info");
    }
}