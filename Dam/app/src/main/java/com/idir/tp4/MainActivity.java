package com.idir.tp4;

import android.content.Intent;
import android.os.Bundle;

import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;

import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.idir.tp4.Tp4.Contact;
import com.idir.tp4.Tp4.Tp4;
import com.idir.tp4.databinding.ActivityMainBinding;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View root = View.inflate(this , R.layout.activity_main,null);


        Button tp1Button = root.findViewById(R.id.button_tp1);
        tp1Button.setOnClickListener(view -> {
            Intent i = new Intent(this , Tp1.class);
            startActivity(i);
        });


        Button tp4Button = root.findViewById(R.id.button_tp4);
        tp4Button.setOnClickListener(view -> {
            Intent i = new Intent(this,Tp4.class);
            startActivity(i);
        });

        setContentView(root);

    }

}