
package com.example.response.service;

import org.springframework.stereotype.Service;

@Service
public class SqsResponseListener {

    public void handleResponse(String message) {
        // Mock: Update DynamoDB record with PMT-PROCESSED
    }
}
