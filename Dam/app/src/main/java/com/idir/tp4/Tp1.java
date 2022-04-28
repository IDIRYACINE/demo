package com.idir.tp4;

import android.app.Activity;
import android.os.Bundle;

import android.view.View;

public class Tp1 extends Activity {


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View root = View.inflate(this,R.layout.activity_tp1, null);
        setContentView(root);

    }

}