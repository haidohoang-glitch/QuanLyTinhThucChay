# Stored Procedure: `prc_asd_QLTC_GetContractNo_ContractDetails`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.337000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@p_ContractNo` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		dinhlv
-- Create date: 2022-01-13
-- Description:	Lấy thông tinchi tiet hop dong
--  prc_asd_GetContractNo_Contract 'QC0011019'
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_QLTC_GetContractNo_ContractDetails]
    @p_ContractNo NVARCHAR(MAX) = NULL --'QC920211,QC1320211,PC050111'
AS
BEGIN
    SELECT ct.HopDongID ID, ct.SoHopDong CONTRACT_NUMBER, ctd.HopDongChiTietID PhanBoId FROM dbo.HopDong ct
            JOIN dbo.HopDongChiTiet ctd ON ct.HopDongID = ctd.HopDongFK AND ctd.DeletedStatus = 0
    WHERE   ct.DeletedStatus = 0
            AND ct.SoHopDong IN (SELECT [name] FROM STRING_SPLIT_QLTC(@p_ContractNo));
END;   

```
