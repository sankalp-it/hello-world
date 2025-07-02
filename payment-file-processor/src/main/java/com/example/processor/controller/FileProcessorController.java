
package com.example.processor.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;
import io.awspring.cloud.messaging.listener.annotation.SqsListener;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

@Component
public class FileProcessorController {

    private final KafkaTemplate<String, String> kafkaTemplate;

    @Value("#{${file.topic.map}}")
    private Map<String, String> prefixToTopicMap;

    public FileProcessorController(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @SqsListener("file-upload-queue")
    public void receiveMessage(@Payload String message) {
        System.out.println("Received SQS message: " + message);

        StringTokenizer tokenizer = new StringTokenizer(message, ",");
        String filename = tokenizer.hasMoreTokens() ? tokenizer.nextToken() : null;
        String s3url = tokenizer.hasMoreTokens() ? tokenizer.nextToken() : null;

        if (filename != null) {
            for (Map.Entry<String, String> entry : prefixToTopicMap.entrySet()) {
                if (filename.startsWith(entry.getKey())) {
                    kafkaTemplate.send(entry.getValue(), message);
                    System.out.println("Published to topic: " + entry.getValue());
                    break;
                }
            }
        }
    }
}
