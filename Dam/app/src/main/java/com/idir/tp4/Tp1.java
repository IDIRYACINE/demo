package com.idir.tp4;

import android.app.Activity;
import android.os.Bundle;

import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Tp1 extends Activity {

    private EditText nameField,surnameField,addressField;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View root = View.inflate(this,R.layout.activity_tp1, null);

        nameField = root.findViewById(R.id.name_field);
        surnameField = root.findViewById(R.id.surname_field);
        addressField = root.findViewById(R.id.address_field);

        Button confirmButton = root.findViewById(R.id.confirm_button);
        confirmButton.setOnClickListener(view -> {
            String name = nameField.getText().toString();
            String surname = surnameField.getText().toString();
            Toast.makeText(getApplicationContext(),name + " " + surname,Toast.LENGTH_SHORT).show();

        });

        setContentView(root);

    }

}