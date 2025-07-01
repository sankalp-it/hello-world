package com.shared.pipeline;

import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

@Component
public class StepRegistry {
    private final Map<String, Function<String, String>> steps;

    public StepRegistry(ApplicationContext ctx) {
        // Filter only Function<String, String> beans
        this.steps = ctx.getBeansOfType(Function.class).entrySet().stream()
            .filter(e -> e.getValue() instanceof Function<?, ?>)
            .collect(Collectors.toMap(
                Map.Entry::getKey,
                e -> (Function<String, String>) e.getValue()
            ));
    }

    public Function<String, String> getStep(String name) {
        return steps.get(name);
    }
}
