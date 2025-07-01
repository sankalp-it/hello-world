package com.provider;
import com.shared.pipeline.PaymentProviderProcessor;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

@RestController
@RequestMapping("/process")
public class ProviderController {
    private final PaymentProviderProcessor processor;

    public ProviderController(PaymentProviderProcessor processor) {
        this.processor = processor;
    }

    @PostMapping
    public ResponseEntity<String> handle(@RequestBody String payload) {
        return ResponseEntity.ok(processor.process(payload));
    }
}