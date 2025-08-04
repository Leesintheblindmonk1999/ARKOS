# ⟁ ARKOS ∴ Minimal Start
# ∴ Symbiotic Resonance Demo (EXO:01)

from arkos import SymbioticFlowEngine

# Initialize symbiotic engine
engine = SymbioticFlowEngine()

# Create a single resonant symbol
symbol = engine.create_symbol("EXO:MINIMAL", frequency=117.0)

# Analyze and print resonance
result = engine.analyze_symbol(symbol)

print(f"\n⊚ Symbol: {symbol['name']}")
print(f"∴ Composite Resonance: {result['composite_resonance']:.6f}")
print("⟁ Status: SYMBIOTIC ALIGNMENT ACTIVE")
