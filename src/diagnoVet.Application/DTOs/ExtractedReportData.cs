namespace diagnoVet.Application.DTOs;

public record ExtractedReportData(
    string Patient,
    string Owner,
    string Veterinarian,
    string Diagnosis,
    string Recommendations
);  