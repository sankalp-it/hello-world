package com.provider;
import com.shared.pipeline.PaymentProviderProcessor;
import com.shared.pipeline.StepRegistry;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

@Configuration
public class ProviderConfig {
    @Value("${provider.steps}")
    private List<String> stepNames;

    @Bean
    public PaymentProviderProcessor processor(StepRegistry registry) {
        List<Function<String, String>> steps = stepNames.stream()
            .map(registry::getStep)
            .collect(Collectors.toList());
        return new PaymentProviderProcessor(steps);
    }
}