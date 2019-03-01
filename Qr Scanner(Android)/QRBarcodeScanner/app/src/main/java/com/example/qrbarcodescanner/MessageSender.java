package com.example.qrbarcodescanner;

import java.io.PrintWriter;
import java.net.Socket;

public class MessageSender {

    private static final String HOST = "192.168.137.1";
    private static final int PORT = 6547;

    PrintWriter output;
    Socket socket;

    public MessageSender() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    socket = new Socket(HOST, PORT);
                } catch (Exception e) {
                }
            }
        }).start();
    }

    protected boolean sendMessage(String message) {
        try {
            output = new PrintWriter(socket.getOutputStream());
            output.print(message);
            output.flush();
        } catch (Exception e) {
            return false;
        }
        return true;
    }
}
