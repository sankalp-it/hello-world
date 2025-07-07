package com.shared.pipeline;

import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Component;

import main.java.com.shared.pipeline.PaymentProcessStep;

@Component
public class StepRegistry {
    private final Map<String, PaymentProcessStep> steps;

    // public StepRegistry(ApplicationContext ctx) {
    //     // Filter only Function<String, String> beans
    //     this.steps = ctx.getBeansOfType(Function.class).entrySet().stream()
    //         .filter(e -> e.getValue() instanceof Function<?, ?>)
    //         .collect(Collectors.toMap(
    //             Map.Entry::getKey,
    //             e -> (Function<String, String>) e.getValue()
    //         ));
    // }
    @Autowired
    public StepRegistry(List<PaymentProcessStep> steps) {
        for (PaymentProcessStep step : steps) {
            steps.put(step.getStepName(), step);
        }
    }

    public String getStep(String name) {
        return steps.get(name);
    }
    // public Function<String, String> getStep(String name) {
    //     return steps.get(name);
    // }
}
