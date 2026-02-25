from sqlalchemy import Table, Column, Integer, String, Numeric, Date, ForeignKey, MetaData, func, CheckConstraint, Enum
from schemas import ContractStatus

metadata_obj = MetaData()

clients_model = Table('clients',
                      metadata_obj,
                      Column('client_id', Integer, primary_key=True),
                      Column('first_name', String(64), nullable=False),
                      Column('last_name', String(64), nullable=False),
                      Column('address', String(256), nullable=False),
                      Column('phone_number', String(20), nullable=False),
                      Column('email', String(128), nullable=False))

departments_model = Table('department',
                      metadata_obj,
                      Column('department_id', Integer, primary_key=True),
                      Column('name', String(128), nullable=False),
                      Column('address', String(256), nullable=False),
                      Column('phone_number', String(20), nullable=False))

employees_model = Table('employee',
                      metadata_obj,
                Column('employee_id', Integer, primary_key=True),
                      Column('first_name', String(64), nullable=False),
                      Column('last_name', String(64), nullable=False),
                      Column('phone_number', String(20), nullable=False),
                      Column('hire_date', Date, server_default=func.current_date()),
                      Column('department_id', Integer, ForeignKey('department.department_id'))
                        )
contracts_model = Table('contract',
                      metadata_obj,
                      Column('contract_id', Integer, primary_key=True),
                      Column('status', Enum(ContractStatus), nullable= False),
                      Column('start_date', Date, nullable=False, server_default= func.current_date()),
                      Column('end_date', Date, nullable=False),
                      CheckConstraint('start_date<end_date', name = 'check_dates'), # как указать check(start_date<end_date)
                      Column('coverage_amount', Numeric(15,2), nullable=False),
                      Column('premium_amount', Numeric(15,2), nullable=False),
                      Column('policy_type', String(128), nullable=False),
                      Column('employee_id', Integer, ForeignKey('employee.employee_id')),
                      Column('client_id', Integer, ForeignKey('clients.client_id'))
                             )

