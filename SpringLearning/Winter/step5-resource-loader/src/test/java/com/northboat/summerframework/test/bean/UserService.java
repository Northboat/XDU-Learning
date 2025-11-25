package com.northboat.summerframework.test.bean;


public class UserService {

    private String uId;

    private UserDao userDao;

    public UserService(String uId) {
        this.uId = uId;
    }

    public void setName(String name) {
        this.uId = name;
    }

    public void queryUserInfo(){
        System.out.println("Querying user info of " + uId + ": " + userDao.queryUserName(uId) );
    }
}