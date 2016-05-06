package com.company;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by y-wu on 2016/05/06.
 */
public class Question344Test {

    @Test
    public void reverseString() throws Exception {
        Question344 q = new Question344();

        Assert.assertEquals("message", "emoclew", q.reverseString("welcome"));

        Assert.assertEquals("message", "olleh", q.reverseString("hello"));

        Assert.assertEquals("message", "metsys", q.reverseString("system"));
    }

}