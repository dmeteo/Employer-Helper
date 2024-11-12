using MediatR;

namespace EmployeeHelper.UseCases.Registration;

public record RegistrationCommand(string FirstName, string LastName, string Surname, string Email, string PhoneNumber, string Password) : IRequest<Unit>;
