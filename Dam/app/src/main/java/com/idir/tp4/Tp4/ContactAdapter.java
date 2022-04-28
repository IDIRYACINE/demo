package com.idir.tp4.Tp4;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;

import com.idir.tp4.R;

import java.util.ArrayList;

public class ContactAdapter extends BaseAdapter {
    private final Context context;
    private final ArrayList<Contact> data;

    public ContactAdapter(Context context, ArrayList<Contact> data) {
        this.context = context;
        this.data = data;
    }

    @Override
    public int getCount() {
        return data.size();
    }

    @Override
    public Contact getItem(int i) {
        return data.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @SuppressLint("ViewHolder")
    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        Contact contact = getItem(i);

        LayoutInflater inflater = LayoutInflater.from(context);
        view = inflater.inflate(R.layout.widget_contacts,viewGroup,false);

        TextView phoneField = view.findViewById(R.id.contact_phone);
        phoneField.setText(contact.getPhone());

        TextView nameField = view.findViewById(R.id.contact_name);
        nameField.setText(contact.getName());

        ImageButton callBtn = view.findViewById(R.id.call_btn);
        callBtn.setOnClickListener(view1 -> makeCall(contact.getPhone()));

        return view;
    }

    private void makeCall(String phone){
        Intent i = new Intent(Intent.ACTION_DIAL,Uri.parse(phone));
        context.startActivity(i);
    }
}
