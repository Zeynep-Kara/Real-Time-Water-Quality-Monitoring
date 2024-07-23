# Real-Time Water Quality Monitoring and Machine Learning Predictions

## Experimental Setup

The experimental setup aimed to measure real-time water quality by monitoring different concentrations of NaCl and MgSO4 in water samples. The setup included the following components:

### Components

1. **Analog Discovery 2 Device**: This device was used to collect impedance data from water samples. It generates an AC signal that sweeps across a range of frequencies from 1 kHz to 1 MHz in 201 steps, measuring the resulting voltage drop and current passing through the sample.

2. **Drip Mechanism**:
    - **Cup and Tube Arrangement**: A long, thin tube was attached to the bottom of a cup to achieve a constant drip-rate. The height difference between the start and end of the experiment was minimized, ensuring a steady flow rate throughout the experiment.
    - **Water Height Measurement**: The initial and final heights of the water were measured to ensure consistency. The heights were recorded at 62.1 cm and 60.7 cm, respectively.
    - **Toricelli’s Law**: The speed of water flowing out of a small hole due to gravity was calculated using Toricelli’s Law (\(v_{\text{drip}} = \sqrt{2gh}\)), which indicated a total speed difference of approximately 1.14% from the last to the first drop.

3. **Mixing Mechanism**:
    - **Aquarium Motor**: To ensure consistent mixing of solutions, an aquarium motor was used. This prevented non-homogenization issues, where denser saltwater could sink to the bottom, leading to unusable measurements. The motor was thoroughly cleaned before each experiment.

4. **Solutions and Experiments**:
    - **Parent Solutions**: These were prepared with target concentrations within a ±300 ppm range. The maximum error for salts was 0.02 g, and for water, it was 3 ml per 100 ml of solution. Using parent solutions reduced measurement noise and increased accuracy.
    - **Experiment Design**: Seven experiments were conducted with different initial NaCl and MgSO4 concentrations in the top and bottom solutions (see Table I for details). The aim was to ensure minimal measurement errors and maximize data reliability.

5. **Measurement Parameters**:
    - The Analog Discovery 2 measured various parameters such as impedance (\(Z\)), impedance phase (\(\theta_Z\)), resistance (\(R\)), reactance (\(X\)), admittance (\(Y\)), admittance phase (\(\theta_Y\)), conductance (\(G\)), susceptance (\(Y_{\text{img}}\)), series capacitance (\(C_s\)), parallel capacitance (\(C_p\)), series inductance (\(L_s\)), parallel inductance (\(L_p\)), dissipation (\(D\)), root mean square voltage (\(V_{\text{rms}}\)), and more. These values reflect the behavior of water at different frequencies based on the concentrations of NaCl and MgSO4.

### Experiment Details

| Experiment |               Top                |                Bottom                  |
|------------|----------------------------------|----------------------------------------|
|     No     |   NaCl (ppm)   |   MgSO4 (ppm)   |     NaCl (ppm)    |     MgSO4 (ppm)    |
|------------|----------------|-----------------|-------------------|--------------------|
| 1          | 50,000         | 0               | 0                 | 0                  |
| 2          | 0              | 50,000          | 0                 | 0                  |
| 3          | 50,000         | 50,000          | 0                 | 0                  |
| 4          | 50,000         | 15,000          | 0                 | 15,000             |
| 5          | 15,000         | 50,000          | 15,000            | 0                  |
| 6          | 38,333         | 3,333           | 5,000             | 20,000             |
| 7          | 3,333          | 38,333          | 20,000            | 5,000              |


#### Experiment Flow

- **Experiments 1 and 2**: These focused on observing the effects of increasing NaCl and MgSO4 alone in respective solutions.
- **Experiment 3**: This observed the effects of increasing both solutes in the same solution.
- **Experiments 4 and 5**: These explored the effects of increasing one solute while the other solute remained constant.
- **Experiments 6 and 7**: These looked at the effects of one solute increasing in concentration while the other decreased.

#### Experiment Order

The experiments were carried out in the order: 4, 6, 1, 3, 2, 7, 5. This sequence was chosen to detect any potential outside influences, like probe corrosion, by conducting similar experiments some time apart. Previous tests had shown that corrosion of low-cost steel probes could cause unusable measurements, so the experiments were completed within 3 hours to minimize such factors.

### Data Collection and Processing

- **Feature Selection**: Important features such as impedance, impedance phase, resistance, and conductance were selected for machine learning models based on their relevance to water quality analysis and ion concentration measurements.
- **Data Normalization**: Mean normalization and data flattening were applied to the selected features to negate linear relations easily affected by the setup and environment.

## Machine Learning Models

- **Random Forest (RF) Regression**: This algorithm was used to predict the concentrations of NaCl and MgSO4. It performed well across various feature sets, with lower mean absolute errors (MAE).
- **Multilayer Perceptron (MLP)**: This neural network was also implemented but showed higher MAEs compared to the RF algorithm.

The experimental setup, combined with the machine learning models, demonstrated the efficacy of real-time water quality monitoring using impedance spectroscopy, significantly improving prediction accuracy for NaCl and MgSO4 concentrations.
