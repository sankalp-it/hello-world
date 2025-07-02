
package com.example.processor.service;

import org.springframework.stereotype.Service;

@Service
public class FileProcessingService {

    public void processFile(String filePath) {
        // Mock: Read file line-by-line, parse, save to DynamoDB, publish Kafka message
    }
}
