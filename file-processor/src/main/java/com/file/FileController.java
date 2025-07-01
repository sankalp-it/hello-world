package com.file;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.*;
import java.util.concurrent.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/file")
public class FileController {
    private final RestTemplate restTemplate = new RestTemplate();
    private final ExecutorService executor = Executors.newFixedThreadPool(10);

    @PostMapping("/upload")
    public ResponseEntity<Map<String, Object>> upload(@RequestBody List<Map<String, String>> records) {
        List<Future<Map<String, String>>> futures = records.stream().map(record -> executor.submit(() -> {
            String provider = record.get("provider");
            String payload = record.get("payload");
            String url = "http://provider-" + provider + ":8080/process";
            try {
                String response = restTemplate.postForObject(url, payload, String.class);
                return Map.of("status", "success", "provider", provider, "response", response);
            } catch (Exception e) {
                return Map.of("status", "failure", "provider", provider, "error", e.getMessage());
            }
        })).collect(Collectors.toList());

        List<Map<String, String>> results = futures.stream().map(f -> {
            try {
                return f.get();
            } catch (Exception e) {
                return Map.of("status", "failure", "error", "Execution error");
            }
        }).collect(Collectors.toList());

        return ResponseEntity.ok(Map.of("results", results));
    }
}