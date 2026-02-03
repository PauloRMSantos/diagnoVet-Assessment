using diagnoVet.Application.Interfaces;
using diagnoVet.Application.UseCases;
using diagnoVet.Infrastructure.Test;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddControllers();

builder.Services.AddOpenApi();

builder.Services.AddScoped<IFileStorage, TestStorage>();
builder.Services.AddScoped<IDocumentProcessor, TestDocumentProcessor>();
builder.Services.AddScoped<IReportRepository, InMemoryReport>();

builder.Services.AddScoped<UploadReportUseCase>();
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();
app.MapControllers();
app.Run();