package com.northboat.summerframework.test.bean;

import java.util.HashMap;
import java.util.Map;

public class UserDao {
    private final static Map<String, String> hashMap = new HashMap<>();

    static {
        hashMap.put("10001", "northboat");
        hashMap.put("10002", "summer");
        hashMap.put("10003", "framework");
    }

    public String queryUserName(String uid){
        return hashMap.get(uid);
    }
}
