package com.idir.tp4.Tp4;

import android.app.Activity;
import android.os.Bundle;

import android.util.Log;
import android.view.View;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

import com.idir.tp4.R;

import java.util.ArrayList;


public class Tp4 extends Activity {

    private ArrayList<Contact> contacts ;
    private EditText contactNameField ;
    private EditText contactPhoneField ;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        View root =  View.inflate(this,R.layout.activity_tp4, null);

        contactNameField = root.findViewById(R.id.contact_name_field);
        contactPhoneField = root.findViewById(R.id.contact_phone_field);

        contacts = new ArrayList<>();
        ListView contactsView = root.findViewById(R.id.contacts_listView);
        ContactAdapter adapter = new ContactAdapter(this,contacts);
        contactsView.setAdapter(adapter);

        Button addContact = root.findViewById(R.id.contact_add);
        addContact.setOnClickListener(view -> {
            String name = contactNameField.getText().toString();
            String phone = contactPhoneField.getText().toString();

            Contact contact = new Contact(name,phone);
            contacts.add(contact);

            adapter.notifyDataSetChanged();
        });

        setContentView(root);


    }

}