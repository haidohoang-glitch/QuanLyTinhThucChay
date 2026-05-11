# Stored Procedure: `Gen_InsertOrUpdate_CongNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:59.630000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.420000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@CongNoID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHoaDon` | `nvarchar(400)` | No |
| `@NgayXuat` | `datetime(8)` | No |
| `@GiaTri` | `float(8)` | No |
| `@GiaTriThanhToan` | `float(8)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@HanThanhToanID` | `int(4)` | No |
| `@NgayTraHoaDon` | `datetime(8)` | No |
| `@IsSoPhieuThu` | `int(4)` | No |
| `@SoHoaDonGiamTru` | `nvarchar(400)` | No |
| `@SoBangThongKe` | `nvarchar(400)` | No |
| `@NgayChuyenChoKeToan` | `datetime(8)` | No |
| `@Sign` | `int(4)` | No |
| `@PhieuThuLinkNapTien` | `nvarchar(400)` | No |
| `@TaiKhoanKhachHangREF` | `bigint(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Active` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `nvarchar(400)` | No |
| `@PrintStatus` | `nvarchar(400)` | No |
| `@RecordStatus` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_CongNo] 	
@CongNoID int ,	
@HopDongREF int ,	
@SoHoaDon nvarchar (200) ,	
@NgayXuat datetime ,	
@GiaTri float ,	
@GiaTriThanhToan float ,	
@NgayThanhToan datetime ,	
@HanThanhToanID int ,	
@NgayTraHoaDon datetime ,	
@IsSoPhieuThu int ,	
@SoHoaDonGiamTru nvarchar (200) ,	
@SoBangThongKe nvarchar (200) ,	
@NgayChuyenChoKeToan datetime ,	
@Sign int ,	
@PhieuThuLinkNapTien nvarchar (200) ,	
@TaiKhoanKhachHangREF bigint ,	
@GhiChu nvarchar (200) ,	
@Active nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus nvarchar (200) ,	
@PrintStatus nvarchar (200) ,	
@RecordStatus nvarchar (200) 	
As 	
if(exists(select * from [CongNo] where [CongNoID] = @CongNoID))	
UPDATE [dbo].[CongNo] SET 	
[HopDongREF] = @HopDongREF,	
[SoHoaDon] = @SoHoaDon,	
[NgayXuat] = @NgayXuat,	
[GiaTri] = @GiaTri,	
[GiaTriThanhToan] = @GiaTriThanhToan,	
[NgayThanhToan] = @NgayThanhToan,	
[HanThanhToanID] = @HanThanhToanID,	
[NgayTraHoaDon] = @NgayTraHoaDon,	
[IsSoPhieuThu] = @IsSoPhieuThu,	
[SoHoaDonGiamTru] = @SoHoaDonGiamTru,	
[SoBangThongKe] = @SoBangThongKe,	
[NgayChuyenChoKeToan] = @NgayChuyenChoKeToan,	
[Sign] = @Sign,	
[PhieuThuLinkNapTien] = @PhieuThuLinkNapTien,	
[TaiKhoanKhachHangREF] = @TaiKhoanKhachHangREF,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [CongNoID] = @CongNoID	
else 	
INSERT INTO [dbo].[CongNo] (	
[CongNoID],	
[HopDongREF],	
[SoHoaDon],	
[NgayXuat],	
[GiaTri],	
[GiaTriThanhToan],	
[NgayThanhToan],	
[HanThanhToanID],	
[NgayTraHoaDon],	
[IsSoPhieuThu],	
[SoHoaDonGiamTru],	
[SoBangThongKe],	
[NgayChuyenChoKeToan],	
[Sign],	
[PhieuThuLinkNapTien],	
[TaiKhoanKhachHangREF],	
[GhiChu],	
[Active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@CongNoID,	
@HopDongREF,	
@SoHoaDon,	
@NgayXuat,	
@GiaTri,	
@GiaTriThanhToan,	
@NgayThanhToan,	
@HanThanhToanID,	
@NgayTraHoaDon,	
@IsSoPhieuThu,	
@SoHoaDonGiamTru,	
@SoBangThongKe,	
@NgayChuyenChoKeToan,	
@Sign,	
@PhieuThuLinkNapTien,	
@TaiKhoanKhachHangREF,	
@GhiChu,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
