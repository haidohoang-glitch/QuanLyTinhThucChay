# Stored Procedure: `sp_check_muangoai_DTKhacPBKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-12-30 17:58:22.353000
- **Ngày sửa cuối**: 2022-12-30 18:08:07.950000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_check_muangoai_DTKhacPBKy]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	    ---------------check dữ liệu mua ngoài có thông tin dự toán không khớp với phân bổ ký -- THAONP-----------
SELECT c.SoHopDong,
       a.PhanBoId,
       b.SoLuong,
       dbo.FormatNumber(b.DonGia) PBDonGia,
       b.ChietKhau,
       dbo.FormatNumber(b.ThanhTien) PBThanhTien,
	   b.LastModifiedAt,
       a.SoLuong,
       dbo.FormatNumber(a.DonGia) DTDonGia,
       a.ChietKhau,
       dbo.FormatNumber(a.ThanhTien) DTThanhTien,
	   a.LastModificationTime,
       dbo.FormatNumber(b.ThanhTien - a.ThanhTien) AS LechPB_DT
FROM [ASDAG2].PMS.dbo.B_DuToan_ChiTiet a
    JOIN HopDongChiTiet b
        ON a.PhanBoId = b.HopDongChiTietID
    JOIN HopDong c
        ON c.HopDongID = b.HopDongFK
WHERE a.ThanhTien != b.ThanhTien
      AND b.DeletedStatus = 0
      AND YEAR(a.CreationTime) >= 2021
      AND a.IsDeleted = 0
      AND
      (
          b.ThanhTien - a.ThanhTien > 10
          OR b.ThanhTien - a.ThanhTien < -10
      )
GROUP BY c.SoHopDong,
         a.PhanBoId,
         b.SoLuong,
         b.DonGia,
         b.ChietKhau,
         b.ThanhTien,
		 b.LastModifiedAt,
         a.SoLuong,
         a.DonGia,
         a.ChietKhau,
         a.ThanhTien,
		 a.LastModificationTime;
END

```
