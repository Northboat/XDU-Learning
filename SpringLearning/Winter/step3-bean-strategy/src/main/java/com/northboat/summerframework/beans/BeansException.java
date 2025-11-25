package com.northboat.summerframework.beans;

public class BeansException extends RuntimeException {

    public BeansException(String message) {
        super(message);
    }

    public BeansException(String msg, Throwable cause) {
        super(msg, cause);
    }
}
