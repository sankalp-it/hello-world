package com.example.payment.service;

import org.springframework.stereotype.Service;

import com.shared.pipeline.PaymentProviderProcessor;

@Service
public class PaymentMessageProcessor {

    PaymentProviderProcessor providerProcessor;
    @KafkaListener(topicPattern = "#{@topicProvider.getTopic()}")
    public void processPayment(String message) {
        // Your payment processing logic here
        providerProcessor.process(message);
    }
}